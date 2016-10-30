#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        map<int, int> hashmap;
        for (int i = 0; i < nums.size(); i++) {
            if (hashmap.find(nums[i]) != hashmap.end()) {
                // 找一找是否有需要当前的数，找到则取出索引与当前索引配对返回
                auto result = new vector<int>;
                result->push_back(hashmap[nums[i]]);
                result->push_back(i);
                return *result;
            } else {
                hashmap[target - nums[i]] = i;  // 将需要的另一个数为索引存在哈希表里，值为当前数的 index
            }
        }
        return vector<int>();
    }
};