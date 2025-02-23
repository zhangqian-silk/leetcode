package main

import (
	"fmt"
	"math/rand"
)

/*
	不使用任何库函数，设计一个 跳表 。

	跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

	例如，一个跳表包含 [30, 40, 50, 60, 70, 90] ，然后增加 80、45 到跳表中，以下图的方式操作：

	跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。

	了解更多 : https://oi-wiki.org/ds/skiplist/

	在本题中，你的设计应该要包含这些函数：

	bool search(int target) : 返回target是否存在于跳表中。
	void add(int num): 插入一个元素到跳表。
	bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
	注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

	示例 1:

		输入
		["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
		[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
		输出
		[null, null, null, null, false, null, true, false, true, false]

		解释
		Skiplist skiplist = new Skiplist();
		skiplist.add(1);
		skiplist.add(2);
		skiplist.add(3);
		skiplist.search(0);   // 返回 false
		skiplist.add(4);
		skiplist.search(1);   // 返回 true
		skiplist.erase(0);    // 返回 false，0 不在跳表中
		skiplist.erase(1);    // 返回 true
		skiplist.search(1);   // 返回 false，1 已被擦除

	提示:

	0 <= num, target <= 2 * 10^4
	调用search, add,  erase操作次数不大于 5 * 10^4

	link: https://leetcode.cn/problems/design-skiplist/description/
*/

type skiplistNode struct {
	left  *skiplistNode
	right *skiplistNode
	down  *skiplistNode
	level int
	value int
}

type Skiplist struct {
	headNodes []*skiplistNode
}

func Constructor_1206() Skiplist {
	return Skiplist{}
}

func (this *Skiplist) Search(target int) bool {
	res := this.searchNode(target)
	if res != nil {
		return true
	}
	return false
}

func (this *Skiplist) searchNode(target int) *skiplistNode {
	var curNode *skiplistNode
	// 遍历首节点列表，找到一个值小于等于当前节点的首节点
	for i := len(this.headNodes) - 1; i >= 0; i-- {
		headNode := this.headNodes[i]
		if headNode != nil && headNode.value <= target {
			curNode = this.headNodes[i]
			break
		}
	}

	// 从当前首节点出发，向下或向右遍历
	for curNode != nil && curNode.value < target {
		if curNode.right != nil && curNode.right.value <= target {
			curNode = curNode.right
		} else {
			curNode = curNode.down
		}
	}
	if curNode == nil {
		return nil
	} else if curNode.value == target {
		return curNode
	}
	return nil
}

func (this *Skiplist) Add(num int) {
	level := randomLevel()
	var extraHeadNodes []*skiplistNode
	var laseNewNode *skiplistNode
	var curNode *skiplistNode
	for i := level; i > 0; i-- {
		newNode := &skiplistNode{level: i, value: num}
		if laseNewNode != nil {
			laseNewNode.down = newNode
		}
		laseNewNode = newNode

		if i > len(this.headNodes) {
			// 目前所有索引层次比该节点要低，先加入临时列表中
			// 再倒序统一添加至头节点列表
			extraHeadNodes = append(extraHeadNodes, newNode)
		} else {
			if curNode == nil {
				// curNode 为空，取该层级的头节点
				headNode := this.headNodes[i-1]
				if headNode == nil || (headNode != nil && headNode.value > num) {
					// 新节点为新的首节点
					newNode.right = headNode
					this.headNodes[i-1] = newNode
					if headNode != nil {
						headNode.left = newNode
					}
					continue
				}

				// 其他情况，说明新节点一定不是该层以及下面层的首节点，开始从 curNode 开始遍历
				curNode = headNode
			}

			// 遍历查找要插入的位置，直到找到大于当前节点的元素或找到结尾
			for curNode.right != nil && curNode.right.value < num {
				curNode = curNode.right
			}
			// 遍历结束后，将新节点插入至 curNode 右侧
			newNode.right = curNode.right
			newNode.left = curNode
			if newNode.right != nil {
				newNode.right.left = newNode
			}
			curNode.right = newNode
			curNode = curNode.down
		}
	}

	// 将 extraHeadNodes 中的元素，倒序插入头节点列表
	for i := len(extraHeadNodes) - 1; i >= 0; i-- {
		this.headNodes = append(this.headNodes, extraHeadNodes[i])
	}
	// fmt.Printf("add %d\n", num)
	// this.printDebug()
}

func (this *Skiplist) printDebug() {
	for i := len(this.headNodes) - 1; i >= 0; i-- {
		fmt.Printf("第 %d 层：", i)
		for node := this.headNodes[i]; node != nil; node = node.right {
			fmt.Printf("%d, ", node.value)
		}
	}
	fmt.Printf("\n----------------\n")
}

func (this *Skiplist) Erase(num int) bool {
	node := this.searchNode(num)
	if node == nil {
		return false
	}
	// fmt.Printf("del %d, ", num)
	// 删除该节点
	for node != nil {
		// fmt.Printf("curLevel: %d, ", node.level-1)
		if node.right != nil {
			node.right.left = node.left
		}
		if node.left != nil {
			// 该节点不是首节点
			node.left.right = node.right
			// fmt.Printf("left: %d, ", node.left.value)
		} else {
			this.headNodes[node.level-1] = node.right

		}

		node = node.down
	}
	// fmt.Printf("\n----------------\n")
	return true
}

func randomLevel() int {
	// 限制高度最大为 32，第 n 层的概率为 1/(2^(n+1))
	level := 1
	for level <= 32 && rand.Float64() < 0.25 {
		level++
	}
	return level
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Search(target);
 * obj.Add(num);
 * param_3 := obj.Erase(num);
 */
