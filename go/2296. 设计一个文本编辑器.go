package main

/*
	请你设计一个带光标的文本编辑器，它可以实现以下功能：

	添加：在光标所在处添加文本。
	删除：在光标所在处删除文本（模拟键盘的删除键）。
	移动：将光标往左或者往右移动。
	当删除文本时，只有光标左边的字符会被删除。光标会留在文本内，也就是说任意时候 0 <= cursor.position <= currentText.length 都成立。

	请你实现 TextEditor 类：

	TextEditor() 用空文本初始化对象。
	void addText(string text) 将 text 添加到光标所在位置。添加完后光标在 text 的右边。
	int deleteText(int k) 删除光标左边 k 个字符。返回实际删除的字符数目。
	string cursorLeft(int k) 将光标向左移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。
	string cursorRight(int k) 将光标向右移动 k 次。返回移动后光标左边 min(10, len) 个字符，其中 len 是光标左边的字符数目。


	示例 1：

		输入：
		["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
		[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
		输出：
		[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]

		解释：
		TextEditor textEditor = new TextEditor(); // 当前 text 为 "|" 。（'|' 字符表示光标）
		textEditor.addText("leetcode"); // 当前文本为 "leetcode|" 。
		textEditor.deleteText(4); // 返回 4
								// 当前文本为 "leet|" 。
								// 删除了 4 个字符。
		textEditor.addText("practice"); // 当前文本为 "leetpractice|" 。
		textEditor.cursorRight(3); // 返回 "etpractice"
								// 当前文本为 "leetpractice|".
								// 光标无法移动到文本以外，所以无法移动。
								// "etpractice" 是光标左边的 10 个字符。
		textEditor.cursorLeft(8); // 返回 "leet"
								// 当前文本为 "leet|practice" 。
								// "leet" 是光标左边的 min(10, 4) = 4 个字符。
		textEditor.deleteText(10); // 返回 4
								// 当前文本为 "|practice" 。
								// 只有 4 个字符被删除了。
		textEditor.cursorLeft(2); // 返回 ""
								// 当前文本为 "|practice" 。
								// 光标无法移动到文本以外，所以无法移动。
								// "" 是光标左边的 min(10, 0) = 0 个字符。
		textEditor.cursorRight(6); // 返回 "practi"
								// 当前文本为 "practi|ce" 。
								// "practi" 是光标左边的 min(10, 6) = 6 个字符。

	提示：

		1 <= text.length, k <= 40
		text 只含有小写英文字母。
		调用 addText ，deleteText ，cursorLeft 和 cursorRight 的 总 次数不超过 2 * 10^4 次。

	进阶：你能设计并实现一个每次调用时间复杂度为 O(k) 的解决方案吗？

	link: https://leetcode.cn/problems/design-a-text-editor/description/
*/

type textEditorNode struct {
	pre  *textEditorNode
	next *textEditorNode
	char rune
}

type TextEditor struct {
	headNode *textEditorNode
	curNode  *textEditorNode
}

func Constructor_2296() TextEditor {
	headNode := &textEditorNode{
		char: rune('|'),
	}
	return TextEditor{
		headNode: headNode,
		curNode:  headNode,
	}
}

func (t *TextEditor) AddText(text string) {
	for _, ch := range text {
		newNode := &textEditorNode{
			char: ch,
		}

		// 先将新节点与光标左侧节点绑定
		if t.curNode.pre == nil {
			t.headNode = newNode
		} else {
			t.curNode.pre.next = newNode
			newNode.pre = t.curNode.pre
		}

		// 再与光标绑定
		newNode.next = t.curNode
		t.curNode.pre = newNode
	}
	t.debugPrint()
}

func (t *TextEditor) DeleteText(k int) int {
	curNode := t.curNode.pre
	if curNode == nil {
		// 光标左侧没有字符
		return 0
	}

	res := 0
	for res < k {
		res++

		if curNode.pre == nil {
			// 当前字符左侧为空，直接将头节点修改为光标节点
			t.headNode = t.curNode
			t.curNode.pre = nil
			break
		}

		curNode.pre.next = t.curNode
		t.curNode.pre = curNode.pre
		curNode = curNode.pre
	}
	t.debugPrint()
	return res
}

func (t *TextEditor) CursorLeft(k int) string {
	for i := 0; i < k; i++ {
		if t.curNode.pre == nil {
			// 无法移动
			break
		}

		preNode := t.curNode.pre
		preNode.next = t.curNode.next
		if t.curNode.next != nil {
			t.curNode.next.pre = preNode
		}
		if preNode.pre != nil {
			preNode.pre.next = t.curNode
		}
		t.curNode.pre = preNode.pre
		preNode.pre = t.curNode
		t.curNode.next = preNode
	}
	t.debugPrint()
	return t.leftChar()
}

func (t *TextEditor) CursorRight(k int) string {
	for i := 0; i < k; i++ {
		if t.curNode.next == nil {
			// 无法移动
			break
		}

		nextNode := t.curNode.next
		nextNode.pre = t.curNode.pre
		if t.curNode.pre != nil {
			t.curNode.pre.next = nextNode
		}
		if nextNode.next != nil {
			nextNode.next.pre = t.curNode
		}
		t.curNode.next = nextNode.next
		nextNode.next = t.curNode
		t.curNode.pre = nextNode
	}
	t.debugPrint()
	return t.leftChar()
}

func (t *TextEditor) leftChar() string {
	// 向左查找最多 10 位
	curNode := t.curNode
	for i := 0; i < 10; i++ {
		if curNode.pre == nil {
			break
		}
		curNode = curNode.pre
	}
	if curNode == t.curNode {
		return ""
	}

	var res []rune
	for curNode != t.curNode {
		res = append(res, curNode.char)
		curNode = curNode.next
	}
	return string(res)
}

func (t *TextEditor) debugPrint() {
	// node := t.headNode
	// for node != nil {
	// 	fmt.Printf("%s, ", string(node.char))
	// 	node = node.next
	// }
	// fmt.Printf("\n")
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddText(text);
 * param_2 := obj.DeleteText(k);
 * param_3 := obj.CursorLeft(k);
 * param_4 := obj.CursorRight(k);
 */
