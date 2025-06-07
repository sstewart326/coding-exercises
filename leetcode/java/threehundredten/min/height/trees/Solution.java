package threehundredten.min.height.trees;

import java.util.*;

public class Solution {

    private List<Integer> traverse(Set<Integer> nodes, Set<Integer> remainingNodes, Map<Integer, Set<Integer>> edges) {
        if (remainingNodes.size() <= 2) {
            return new ArrayList<>(remainingNodes);
        }
        for (Integer node : nodes) {
            remainingNodes.remove(node);
            edges.remove(node);
        }

        Set<Integer> leafs = getLeafs(remainingNodes, edges);
        return traverse(leafs, remainingNodes, edges);
    }

    private Set<Integer> getLeafs(Set<Integer> allNodes, Map<Integer, Set<Integer>> edgesMap) {
        Set<Integer> leafs = new HashSet<>();
        for (Integer node : allNodes) {
            Set<Integer> neighbors = edgesMap.get(node);
            int count = 0;
            for (Integer neighbor : neighbors) {
                if (edgesMap.containsKey(neighbor)) {
                    if (count == 1) {
                        count = 0;
                        break;
                    } else {
                        count++;
                    }
                }
            }
            if (count == 1) {
                leafs.add(node);
            }
        }
        return leafs;
    }

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            return List.of(0);
        }

        Map<Integer, Set<Integer>> edgesMap = new HashMap<>();
        Set<Integer> allNodes = new HashSet<>();

        for (int[] e : edges) {
            Integer x = e[0];
            Integer y = e[1];
            allNodes.add(x);
            allNodes.add(y);

            Set<Integer> xNeighbors = edgesMap.getOrDefault(x, new HashSet<>());
            Set<Integer> yNeighbors = edgesMap.getOrDefault(y, new HashSet<>());
            xNeighbors.add(y);
            yNeighbors.add(x);
            edgesMap.put(x, xNeighbors);
            edgesMap.put(y, yNeighbors);
        }

        return traverse(getLeafs(allNodes, edgesMap), allNodes, edgesMap);
    }

}