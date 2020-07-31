ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    },
    {
        'name' : 'Eric'
    }
  ]
}

print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][1]['interests'][1])
print(ramit['friends'][0]['email'])



def countFriends(friends_dict):
    friend_counter = 0
    for x in friends_dict['friends']:
        friend_counter += 1
    
    friends_dict['friends_count'] = friend_counter
    return friends_dict

print(countFriends(ramit))