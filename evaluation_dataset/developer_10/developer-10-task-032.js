function stripRelayConnection(gqlType, queryASTNode, fragments) {
  const edgeType = stripNonNullType(gqlType._fields.edges.type)
  const strippedType = stripNonNullType(stripNonNullType(edgeType.ofType)._fields.node.type)
  const args = queryASTNode.arguments
  const edges = spreadFragments(queryASTNode.selectionSet.selections, fragments, gqlType.name)
    .find(selection => selection.name.value === 'edges')
  if (edges) {
    queryASTNode = spreadFragments(edges.selectionSet.selections, fragments, gqlType.name)
      .find(selection => selection.name.value === 'node') || {}
  } else {
    queryASTNode = {}
  }
  queryASTNode.arguments = args
  return { gqlType: strippedType, queryASTNode }
}