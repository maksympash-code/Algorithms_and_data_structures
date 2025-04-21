from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/longest_sequence', methods=['POST'])
def longest_sequence():
    data = request.get_json()
    input_string = data.get('string', '')

    if not input_string:
        return jsonify({'error': 'No string provided'}), 400

    max_char = input_string[0]
    max_length = current_length = 1

    for ch_prev, ch in zip(input_string, input_string[1:]):
        if ch == ch_prev:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_char = ch
        else:
            current_length = 1

    return jsonify({
        'character': max_char,
        'length': max_length
    })

if __name__ == '__main__':
    app.run(debug=True)
