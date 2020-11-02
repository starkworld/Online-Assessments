public static void main(String[] args) {
	int[][] bids = {{1,5,5,0}, {2,7,8,1}, {3,7,5,1},{4,10,3,3}};
	int totalShares = 18;
	List<Integer> res = getUnallocatedUsers(bids, totalShares);
	System.out.println(res);
}

private static List<Integer> getUnallocatedUsers(int[][] bids, int totalShares) {
	List<Integer> res = new ArrayList<>();
	if(bids == null || bids.length == 0 || totalShares == 0)
		return res;
	Comparator<int[]> bidsComparator = new Comparator<int[]>() {

		@Override // 0. id, 1. num of shares, 2. bidding price, 3. time stamp
		public int compare(int[] o1, int[] o2) {
			if(o1[2] != o2[2])
				return o2[2] - o1[2];
			else if(o1[3] != o2[3])
				return o1[3] - o2[3];
			else if(o1[1] != o2[1])
				return o2[1] - o1[1];
			return 0;
		}
	};

	Queue<int[]> maxHeap = new PriorityQueue<int[]>(bidsComparator);
	for(int[] bid: bids)
		maxHeap.add(bid);
	while(totalShares > 0 && !maxHeap.isEmpty()) {
		totalShares -= maxHeap.peek()[1];
		maxHeap.poll();
	}
	while(!maxHeap.isEmpty())
		res.add(maxHeap.poll()[0]);
	Collections.sort(res);
	return res;
}