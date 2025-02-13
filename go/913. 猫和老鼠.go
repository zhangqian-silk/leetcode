package main

/*
	两位玩家分别扮演猫和老鼠，在一张 无向 图上进行游戏，两人轮流行动。

	图的形式是：graph[a] 是一个列表，由满足 ab 是图中的一条边的所有节点 b 组成。

	老鼠从节点 1 开始，第一个出发；猫从节点 2 开始，第二个出发。在节点 0 处有一个洞。

	在每个玩家的行动中，他们 必须 沿着图中与所在当前位置连通的一条边移动。例如，如果老鼠在节点 1 ，那么它必须移动到 graph[1] 中的任一节点。

	此外，猫无法移动到洞中（节点 0）。

	然后，游戏在出现以下三种情形之一时结束：

	如果猫和老鼠出现在同一个节点，猫获胜。
	如果老鼠到达洞中，老鼠获胜。
	如果某一位置重复出现（即，玩家的位置和移动顺序都与上一次行动相同），游戏平局。
	给你一张图 graph ，并假设两位玩家都都以最佳状态参与游戏：

	如果老鼠获胜，则返回 1；
	如果猫获胜，则返回 2；
	如果平局，则返回 0 。

	示例 1：

		输入：graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
		输出：0

	示例 2：

		输入：graph = [[1,3],[0],[3],[0,2]]
		输出：1

	提示：

		3 <= graph.length <= 50
		1 <= graph[i].length < graph.length
		0 <= graph[i][j] < graph.length
		graph[i][j] != i
		graph[i] 互不相同
		猫和老鼠在游戏中总是可以移动

	link: https://leetcode.cn/problems/cat-and-mouse/description/
*/

func CatMouseGame(graph [][]int) int {
	// 参考：https://leetcode.cn/problems/cat-and-mouse/solutions/1190676/pytuo-bu-pai-xu-ni-xiang-si-wei-by-migea-ie1b/
	type Status struct {
		ini, ip, op int
	}

	type StatusRes struct {
		Status
		result int
	}

	const (
		DRAW  = 0
		WIN   = 1
		LOSE  = 2
		CAT   = 0
		MOUSE = 1
	)

	statusMap := make(map[Status]int)
	out := make(map[Status]int)
	queue := []StatusRes{}

	setResult := func(status Status, result int) {
		statusMap[status] = result
		queue = append(queue, StatusRes{
			Status: status,
			result: result,
		})
	}

	// 存储所有基本状态
	// 1. 猫与鼠在同一个位置，猫先手则必胜，鼠先手则必输
	// 2. 鼠后手在洞中，必胜
	// 3. 猫后手在洞中，因为猫无法进洞，所以认为这种情况猫必输
	for ini := CAT; ini <= MOUSE; ini++ {
		for p := 1; p < len(graph); p++ {
			if ini == CAT {
				setResult(Status{ini, p, p}, WIN)
				setResult(Status{ini, p, 0}, LOSE)
			} else {
				setResult(Status{ini, p, p}, LOSE)
				setResult(Status{ini, p, 0}, WIN)
			}
		}
	}

	// 遍历基础状态，倒推其他状态
	for len(queue) > 0 {
		curStatus := queue[0]
		queue = queue[1:]
		// 遍历基础状态中，后手位置相邻边，得到前一步状态，并计算其 res
		for _, preip := range graph[curStatus.op] {
			// preStatus 在执行一次操作后，ip 会变为其临边的另一端，op 不变
			// 故 curStatus 在变换先后手后，ip 变为了 preStatus 的后手的位
			// 置，即 preStatus.op，op 变为了 ip 操作后的位置
			preStatus := Status{
				ini: 1 ^ curStatus.ini, // 变更先后手
				ip:  preip,             // curStatus 的后手位置的相邻边
				op:  curStatus.ip,      // preStatus 操作后，该后手位置变为 curStatus 的先手位置
			}

			// 过滤重复状态
			if _, ok := statusMap[preStatus]; ok {
				continue
			}

			if curStatus.result == LOSE {
				// 如果当前是必负态，则前一个状态必胜
				setResult(preStatus, WIN)
			} else {
				// 如果当前不是必负态，即平局或必胜，则前一个状态要仅可能避免走到该状态
				// 故此时将前一个状态能够走向的值的数量减一
				cnt, ok := out[preStatus]
				if !ok {
					out[preStatus] = len(graph[preStatus.ip]) - 1
				} else {
					out[preStatus] = cnt - 1
				}
				if out[preStatus] == 0 {
					// 该状态走向的所有状态，均为平局或必胜局，说明该状态无法走向胜利，将其设置为必输态
					setResult(preStatus, LOSE)
				}
			}
		}
	}
	return statusMap[Status{ini: MOUSE, ip: 1, op: 2}]
}
