public static void main(String[] args) {
	int[][] nums1 = {{2,3},{5,7}};
	int[][] nums2 = {{1,1},{2,0}};
	solve(nums1);
	System.out.println("---------------");
	solve(nums2);
}

private static void solve(int[][] nums) {
	int[][] res = new int[nums.length][nums[0].length];
	for(int i=0;i<nums.length;i++) {
		for(int j=0;j<nums[0].length;j++) {
			if(i == 0 && j == 0)
				res[i][j] = nums[i][j];
			else if(i == 0)
				res[i][j] = res[i][j-1] + nums[i][j];
			else if(j == 0)
				res[i][j] = res[i-1][j] + nums[i][j];
			else
				res[i][j] = res[i-1][j] + res[i][j-1] - res[i-1][j-1] + nums[i][j];
		}
	}
	for(int[] row : res)
		System.out.println(Arrays.toString(row));
}