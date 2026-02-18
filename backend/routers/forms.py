from flask import Blueprint, request, jsonify

forms_blueprint = Blueprint('forms', __name__)

# In-memory storage for forms (Replace with database in production)
forms_storage = {}

@forms_blueprint.route('/forms', methods=['POST'])
def create_form():
    form_id = request.json.get('id')
    if form_id in forms_storage:
        return jsonify({'error': 'Form already exists'}), 400
    forms_storage[form_id] = request.json
    return jsonify({'message': 'Form created', 'form': forms_storage[form_id]}), 201

@forms_blueprint.route('/forms/<form_id>', methods=['GET'])
def read_form(form_id):
    form = forms_storage.get(form_id)
    if not form:
        return jsonify({'error': 'Form not found'}), 404
    return jsonify(form), 200

@forms_blueprint.route('/forms/<form_id>', methods=['PUT'])
def update_form(form_id):
    form = forms_storage.get(form_id)
    if not form:
        return jsonify({'error': 'Form not found'}), 404
    forms_storage[form_id] = request.json
    return jsonify({'message': 'Form updated', 'form': forms_storage[form_id]}), 200

@forms_blueprint.route('/forms/<form_id>', methods=['DELETE'])
def delete_form(form_id):
    form = forms_storage.pop(form_id, None)
    if not form:
        return jsonify({'error': 'Form not found'}), 404
    return jsonify({'message': 'Form deleted'}), 204

@forms_blueprint.route('/forms/case/<case_id>', methods=['GET'])
def get_forms_by_case_id(case_id):
    # Assuming case_id is a part of the form data
    filtered_forms = [form for form in forms_storage.values() if form.get('case_id') == case_id]
    return jsonify(filtered_forms), 200

# Note: Don't forget to register the blueprint in your main application file.