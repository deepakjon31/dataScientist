from flask import Flask, render_template, request, url_for, jsonify
from chatbot import *
app = Flask(__name__)


@app.route('/message', methods=['POST'])
def reply():
    print('deepak.....')
    print(request.form['msg'])
    initial_message = "My name is Robo. I will answer your queries. \n\t If you want to exit, type Bye!"
    user_response = ''
    user_response = request.form['msg']
    if (greeting(user_response) != None):
        initial_message = greeting(user_response)
    else:
        initial_message = response(user_response)
        # print(response(user_response))
        sent_tokens.remove(user_response)
    print(user_response, 'Ajax...')

    return jsonify({'text': initial_message}), 200

    # return jsonify({ 'text': execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, request.form['msg'] ) } )


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/chat', methods=['GET'])
# def chat_response():
#     flag = True
#     initial_message = "ROBO: My name is Robo. I will answer your queries. \n\t If you want to exit, type Bye!"
#     user_response = ''

    # if request.method == 'POST':
    #     user_response = request.form['message']
    #     print(user_response)
    #     # while flag:
    #     user_response = user_response.lower()
    #     if (user_response != 'bye'):
    #         if (user_response == 'thanks' or user_response == 'thank you'):
    #             flag = False
    #             print("ROBO: You are welcome..")
    #         else:
    #             if (greeting(user_response) != None):
    #                 initial_message = "ROBO: " + greeting(user_response)
    #             else:
    #                 initial_message = "ROBO: " + response(user_response)
    #                 # print(response(user_response))
    #                 sent_tokens.remove(user_response)
    #
    #     else:
    #         flag = False
    #         print("ROBO: Bye! take care..")
    #
    # if request.method == 'GET':
    #     user_response = request.args.get('message')
    #     if (greeting(user_response) != None):
    #         initial_message = "ROBO: " + greeting(user_response)
    #     else:
    #         initial_message = "ROBO: " + response(user_response)
    #         # print(response(user_response))
    #         sent_tokens.remove(user_response)
    #     print(user_response, 'Ajax...')
    #
    # return jsonify({'user_chat': user_response, 'robo_res': initial_message}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

