function assignChannelsToUsersAndRoles(doc, oldDoc, accessAssignmentDefinition) {
    var usersAndRoles = [ ];
    var users = resolveCollectionDefinition(doc, oldDoc, accessAssignmentDefinition.users);
    for (var userIndex = 0; userIndex < users.length; userIndex++) {
      usersAndRoles.push(users[userIndex]);
    }
    var roles = resolveRoleCollectionDefinition(doc, oldDoc, accessAssignmentDefinition.roles);
    for (var roleIndex = 0; roleIndex < roles.length; roleIndex++) {
      usersAndRoles.push(roles[roleIndex]);
    }
    var channels = resolveCollectionDefinition(doc, oldDoc, accessAssignmentDefinition.channels);
    access(usersAndRoles, channels);
    return {
      type: 'channel',
      usersAndRoles: usersAndRoles,
      channels: channels
    };
  }