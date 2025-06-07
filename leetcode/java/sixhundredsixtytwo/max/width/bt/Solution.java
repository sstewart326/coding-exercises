package sixhundredsixtytwo.max.width.bt;

import util.TreeNode;

import java.util.*;

public class Solution {

    private static class NodeWithIndex {
        private final int index;
        private final TreeNode nodeValue;
        private final int level;

        public NodeWithIndex(int index, TreeNode nodeValue, int level) {
            this.index = index;
            this.nodeValue = nodeValue;
            this.level = level;
        }

        public int getIndex() {
            return index;
        }

        public TreeNode getNodeValue() {
            return nodeValue;
        }

        public int getLevel() {
            return level;
        }
    }

    public int widthOfBinaryTree(TreeNode root) {

        Queue<NodeWithIndex> processingQueue = new LinkedList<>();
        NodeWithIndex node = new NodeWithIndex(1, root, 1);
        processingQueue.add(node);

        int maxWidth = 1;
        Map<Integer, Integer> levels = new HashMap<>();
        while (!processingQueue.isEmpty()) {
            NodeWithIndex n = processingQueue.poll();

            int level = n.getLevel();
            int currWidth = 1;
            if (levels.containsKey(level)) {
                currWidth = Math.abs(n.getIndex() - levels.get(level))+1;
                levels.put(level, Math.min(n.getIndex(), levels.get(level)));
            } else {
                levels.put(level, (n.getIndex()));
            }
            if (currWidth > maxWidth) {
                maxWidth = currWidth;
            }

            if (n.getNodeValue().left != null) {
                NodeWithIndex leftNode = new NodeWithIndex(n.getIndex()*2, n.getNodeValue().left, level+1);
                processingQueue.add(leftNode);
            }
            if (n.getNodeValue().right != null) {
                NodeWithIndex rightNode = new NodeWithIndex((n.getIndex()*2)+1, n.getNodeValue().right, level+1);
                processingQueue.add(rightNode);
            }
        }
        return maxWidth;
    }
}
