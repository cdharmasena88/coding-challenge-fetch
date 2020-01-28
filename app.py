from flask import Flask,  jsonify, request
from flask_restful import Resource, Api
from string import punctuation

app = Flask(__name__)
api = Api(app)


class flaskapp(Resource):
    def get(self):
        return {'flask': 'app'}


def prepareText_ordered(s):
    s = s.replace('\n', '').lower()
    translation = str.maketrans("", "", punctuation)
    s = s.translate(translation)
    s_list = s.split(' ')
    s_mapping = {}

    for i in range(len(s_list)):
        s_mapping[i] = s_list[i]

    return s_mapping, len(s_list)


def prepareText_no_order(s):

    s = s.replace('\n', '').lower()
    translation = str.maketrans("", "", punctuation)
    s = s.translate(translation)
    s_list = s.split(' ')
    s_mapping = {}

    for i in s_list:
        if i not in s_mapping:
            s_mapping[i] = 1
        else:
            s_mapping[i] += 1

    return s_mapping


def compare_orderd(s1, s2):
    s1_dict, s1_word_count = prepareText_ordered(s1)
    s2_dict, s2_word_count = prepareText_ordered(s2)
    similar_word_count = 0
    if s1_word_count > s2_word_count:
        for k, v in s2_dict.items():
            if v == s1_dict[k]:
                similar_word_count += 1
        similarity = (similar_word_count/s1_word_count)
    else:
        for k, v in s1_dict.items():
            if v == s2_dict[k]:
                similar_word_count += 1
        similarity = (similar_word_count/s2_word_count)
    return similarity, similar_word_count


def compare_no_order(s1, s2):
    s1_dict = prepareText_no_order(s1)
    s2_dict = prepareText_no_order(s2)

    similar_words = 0
    if len(s1_dict) < len(s2_dict):
        for k, v in s2_dict.items():
            if k in s1_dict:
                similar_words += 1
        similarity = (similar_words/len(s1_dict))
    else:
        for k, v in s1_dict.items():
            if k in s2_dict:
                similar_words += 1
        similarity = (similar_words/len(s2_dict))

    return similarity, similar_words


@app.route("/comapre_strings", methods=['GET', 'POST'])
def comapre_strings():
    data = request.get_json()
    s1 = data['string1']
    s2 = data['string2']
    order = data['order_of_words']

    if order == "True":
        similarity, similar_word_count = compare_orderd(s1, s2)
    else:
        similarity, similar_word_count = compare_no_order(s1, s2)
    return jsonify({
        'string1': s1,
        'string2': s2,
        'similarity': similarity,
        'similar_word_count': similar_word_count


    })


# @app.route("/comapre_strings_not_orderd", methods=['GET', 'POST'])
# def comapre_strings_not_orderd():
#     data = request.get_json()
#     s1 = data['string1']
#     s2 = data['string2']
#     similarity, similar_word_count = compare_no_order(s1, s2)
#     return jsonify({
#         'string1': s1,
#         'string2': s2,
#         'similarity': similarity,
#         'similar_word_count': similar_word_count


#     })


api.add_resource(flaskapp, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)
