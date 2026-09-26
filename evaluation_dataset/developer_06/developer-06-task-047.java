public static ClusterMember determineMember(
        final ClusterMember[] clusterMembers, final int memberId, final String memberEndpoints)
    {
        ClusterMember member = NULL_VALUE != memberId ? ClusterMember.findMember(clusterMembers, memberId) : null;
        if ((null == clusterMembers || 0 == clusterMembers.length) && null == member)
        {
            member = ClusterMember.parseEndpoints(NULL_VALUE, memberEndpoints);
        }
        else
        {
            if (null == member)
            {
                throw new ClusterException("memberId=" + memberId + " not found in clusterMembers");
            }
            if (!"".equals(memberEndpoints))
            {
                ClusterMember.validateMemberEndpoints(member, memberEndpoints);
            }
        }
        return member;
    }