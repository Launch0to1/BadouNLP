#week3作业

#词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

#待切分文本
sentence = "经常有意见分歧"

#实现全切分函数，输出根据字典能够切分出的所有的切分方式
# # 纯回溯
# def all_cut(sentence, Dict):
#     target = []
#     def cut(start, target_list):
#         if start == len(sentence):
#             target.append(target_list[:])
#             return
#         for key in Dict:
#             if sentence[start:start + len(key)] == key:
#                 target_list.append(key)
#                 cut(start + len(key),target_list)
#                 target_list.pop()
#     cut(0,[])
#     return target

# 动态规划+回溯
def all_cut(sentence,Dict):
    n = len(sentence)

    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1 , -1):
        for j in range(i + 1, n + 1):
            if sentence[i:j] in Dict and dp[j]:
                dp[i] = 1
                break
    
    target = []
    def dfs(start,path):
        if start == n:
            target.append(path[:])
            return
        for end in range(start+1, n+1):
            if sentence[start:end] in Dict and dp[end]:
                path.append(sentence[start:end])
                dfs(end,path)
                path.pop()
    
    dfs(0,[])
    return target


target = all_cut(sentence, Dict)
for i in target:
    print(i) #输出

#目标输出;顺序不重要
target = [
    ['经常', '有意见', '分歧'],
    ['经常', '有意见', '分', '歧'],
    ['经常', '有', '意见', '分歧'],
    ['经常', '有', '意见', '分', '歧'],
    ['经常', '有', '意', '见分歧'],
    ['经常', '有', '意', '见', '分歧'],
    ['经常', '有', '意', '见', '分', '歧'],
    ['经', '常', '有意见', '分歧'],
    ['经', '常', '有意见', '分', '歧'],
    ['经', '常', '有', '意见', '分歧'],
    ['经', '常', '有', '意见', '分', '歧'],
    ['经', '常', '有', '意', '见分歧'],
    ['经', '常', '有', '意', '见', '分歧'],
    ['经', '常', '有', '意', '见', '分', '歧']
]
