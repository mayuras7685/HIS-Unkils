from flask import Flask, request, jsonify
from clarifai.client.model import Model
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
import base64
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Function to get Clarifai PAT
def get_clarifai_pat():
    clarifai_pat_env = os.getenv("CLARIFAI_PAT")
    return clarifai_pat_env


def recognize_food_items(image_bytes, clarifai_pat):
    PAT = clarifai_pat
    USER_ID = 'clarifai'
    APP_ID = 'main'
    MODEL_ID = 'food-item-recognition'
    MODEL_VERSION_ID = '1d5fd481e0cf4826aa72ec3ff049e044'

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)
    metadata = (('authorization', 'Key ' + PAT),)
    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=image_bytes
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    output = post_model_outputs_response.outputs[0]
    food_items = [concept.name for concept in output.data.concepts]
    return food_items


def check_item_match(item_category, input_item_names):
    prompt = f"You are an expert cook. I have passed you an array of food items {input_item_names} and a category {item_category}, tell me if any of the food items in the list is used in the creation of the category item. If any of the food items could be used to make the category item in any way, return a yes. Please give output in boolean form. only use 1 or 0."
    model_prediction = Model("https://clarifai.com/openai/chat-completion/models/gpt-4-turbo").predict_by_bytes(prompt.encode(), input_type="text")
    return bool(model_prediction.outputs[0].data.text.raw)


# Function to calculate cashback
def calculate_cashback(image_bytes, description):
    prompt = f"Does the image {image_bytes} match the description as provided by the user, Description: {description}, list = ['Sorry! Our AI is unable to match the description with the image. Please try with a different description and image.','You have been offered 60% cashback.', 'You have been offered 30% cashback.', 'Please provide another image of damaged food parcel or food.'] If the image doesn't match the description put 1 = 4th list element else If the description seems invalid put 1 = 1st element in list , If the description matches and food's highly damaged then put 1 = 2nd element in 'list', If food's lightly damaged then put 1 = 3rd element in 'list', If the food in the picture or the food parcel is not damaged in the image then put 1 = 4th element in the 'list', generate just the string, no other symbol."
    base64image = base64.b64encode(image_bytes).decode('utf-8')
    inference_params = dict(temperature=0.2, max_tokens=100, image_base64=base64image)
    model_prediction = Model("https://clarifai.com/openai/chat-completion/models/gpt-4-vision").predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)
    return model_prediction.outputs[0].data.text.raw

@app.route('/food-complaint', methods=['POST'])
def food_complaint():
    try:
        # Get data from request
        image_file = request.files['image']
        item_category = request.form['category']
        description = request.form['description']

        # Read image file
        image_bytes = image_file.read()

        # Get Clarifai PAT
        clarifai_pat = get_clarifai_pat()

        # Recognize food items
        food_items = recognize_food_items(image_bytes, clarifai_pat)

        # Check item match
        match = check_item_match(item_category, food_items)

        # Calculate cashback
        cashback = calculate_cashback(image_bytes, description)

        return jsonify({
            'food_items': food_items,
            'match': match,
            'cashback': cashback
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)