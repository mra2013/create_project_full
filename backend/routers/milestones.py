from flask import Blueprint, jsonify, request

# Create a blueprint for the milestone routes
milestone_bp = Blueprint('milestones', __name__)

# In-memory store for milestones (this could be replaced with a database)
milestones = {}
next_id = 1

@milestone_bp.route('/milestones', methods=['POST'])
def create_milestone():
    global next_id
    data = request.json
    title = data.get('title')
    description = data.get('description')
    milestone = {'id': next_id, 'title': title, 'description': description}
    milestones[next_id] = milestone
    next_id += 1
    return jsonify(milestone), 201

@milestone_bp.route('/milestones/<int:milestone_id>', methods=['GET'])
def get_milestone(milestone_id):
    milestone = milestones.get(milestone_id)
    if milestone:
        return jsonify(milestone), 200
    return jsonify({'error': 'Milestone not found'}), 404

@milestone_bp.route('/milestones/<int:milestone_id>', methods=['PUT'])
def update_milestone(milestone_id):
    data = request.json
    milestone = milestones.get(milestone_id)
    if milestone:
        milestone['title'] = data.get('title', milestone['title'])
        milestone['description'] = data.get('description', milestone['description'])
        return jsonify(milestone), 200
    return jsonify({'error': 'Milestone not found'}), 404

@milestone_bp.route('/milestones/<int:milestone_id>', methods=['DELETE'])
def delete_milestone(milestone_id):
    if milestone_id in milestones:
        del milestones[milestone_id]
        return jsonify({'message': 'Milestone deleted'}), 204
    return jsonify({'error': 'Milestone not found'}), 404
