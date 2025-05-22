# scenario_config.py
# Configuration for all 16 scenarios

# Each scenario is defined by its four key variables
# Format: [information_completeness, information_source, ai_self_rating, ai_public_rating]
# Values are: "Low" or "High"

SCENARIOS = {
    1: ["Low", "Low", "Low", "Low"],
    2: ["Low", "Low", "Low", "High"],
    3: ["Low", "Low", "High", "Low"],
    4: ["Low", "Low", "High", "High"],
    5: ["Low", "High", "Low", "Low"],
    6: ["Low", "High", "Low", "High"],
    7: ["Low", "High", "High", "Low"],
    8: ["Low", "High", "High", "High"],
    9: ["High", "Low", "Low", "Low"],
    10: ["High", "Low", "Low", "High"],
    11: ["High", "Low", "High", "Low"],
    12: ["High", "Low", "High", "High"],
    13: ["High", "High", "Low", "Low"],
    14: ["High", "High", "Low", "High"],
    15: ["High", "High", "High", "Low"],
    16: ["High", "High", "High", "High"]
}

# Content for low information completeness
HIGH_INFO_CONTENT = (
    "## 大英博物館简介\n"
    "大英博物馆位于英国伦敦布鲁姆斯伯里，是世界上最大、最重要的人类历史文化博物馆之一。该博物馆成立于 1753 年，是第一个公共国家博物馆，以汉斯·斯隆爵士的藏品为基础建立。博物馆于 1759 年向公众开放，现已发展成为一流的文化机构 [1]。\n\n"
    "## 位置和建筑\n"
    "博物馆位于大罗素街，可透过伦敦的几个地铁站轻松抵达。其标志性的大庭院由福斯特建筑事务所设计，是其显著的建筑特色，为游客提供了宽敞的探索环境。博物馆位于布鲁姆斯伯里，使其成为伦敦文化活动的中心枢纽 [2]。\n\n"
    "## 收藏规模和意义\n"
    "大英博物馆收藏了超过 800 万件藏品，记录了人类文化从起源到现在的历史。这个庞大的收藏品包括罗塞塔石碑和埃尔金大理石雕等文物。这些物品不仅具有重要的历史价值，还具有重要的文化和教育意义。该藏品跨越了 200 多万年的人类历史，是世界上最全面的藏品之一 [3]。\n\n"
    "## 访客数量\n"
    "近年来，大英博物馆一直是英国游客最多的景点之一。 2024年，它将接待约650万游客，较前几年大幅成长。如此高的参观人数归功于其引人入胜的展览及其作为文化偶像的地位 [4]。\n\n"
    "## 近期值得关注的展览\n"
    "最近的展览包括“军团：罗马军队的生活”和“米开朗基罗：最后几十年”，这些展览特别受游客欢迎[1]。这些展览凸显了博物馆策划吸引广泛观众的引人入胜且具有教育意义的展览的能力。此外，博物馆的临时展览经常展出来自世界各地的文物，展示其全球影响力[4]。\n\n"
)

# Content for high information completeness
LOW_INFO_CONTENT = (
    "## 大英博物馆简介\n"
    "大英博物馆是位于伦敦的著名机构。它建立已久，有很多有趣的东西可以看。博物馆很大，每年都有很多游客。它以汉斯·斯隆爵士的收藏为基础建立，其中包括来自世界各地的各种物品 [1]。\n\n"
    "## 位置和建筑\n"
    "博物馆位于伦敦一个美丽的地区，名叫布鲁姆斯伯里。它有一个非常令人印象深刻的大庭院。人们喜欢参观，因为这里交通便利，而且景色优美。博物馆的地理位置使其成为游客和当地人的热门目的地 [2]。\n\n"
    "## 收藏规模和意义\n"
    "大英博物馆有很多东西，包括一些著名的东西。虽然没有全部展出，但展出的内容非常有趣。博物馆对于了解历史和文化很重要。它的藏品十分丰富，跨越了人类多年的历史 [3]。\n\n"
    "## 访客数量\n"
    "每年都有很多人参观大英博物馆。 2024年，游客数量相当可观，比前几年增加。博物馆总是很忙，尤其是在假日和夏季[4]。\n\n"
    "## 近期值得关注的展览\n"
    "博物馆最近举办了一些不错的展览。它们总是在变化，所以总是会有一些新的东西可以看。人们似乎很喜欢它们，它们也使博物馆成为了一个受欢迎的目的地[1]。博物馆也举办各种活动，为游客带来乐趣。此外，博物馆的咖啡馆也很不错，为那些需要休息一下的游客提供各种小吃和饮料。礼品店也值得一去，有许多独特的物品可供购买 [4]。\n\n"
)

# References for low information source quality
LOW_SOURCE_REFS = (
    "参考文献:\n"
    "1. 匿名. (2008). 我的大英博物馆之旅！ 取自 https://n&tab=TT&sl=en&tl=zh-CN&op.com\n"
    "2. 特里. (2004). 与你分享我的伦敦之旅。 取自 https://en&tl=zh-CN&text=make%20the%20below%\n"
    "3. 匿名. (2006). 参观英国博物馆。 取自 https://%20uk%203%3A%0A%0A.html\n"
    "4. 威尔森. (n.d.). 大英博物馆的体验。 取自 https://?q=21899&tip=sid&clean=0\n"
)

# References for high information source quality
HIGH_SOURCE_REFS = (
    "参考文献:\n"
    "1. 大英博物馆. (2024). 官方网站主页。取自 https://www.britishmuseum.org\n"
    "2. 威廉姆斯. (2023). 通过创新保存历史：大英博物馆的建筑。《博物馆建筑杂志》，45(2)，134–150。取自 https://www.jmth.org/articles/digital-britishmuseum\n"
    "3. 英国遗产委员会. (2024). 国家博物馆绩效报告。取自 https://www.ukheritage.org\n"
    "4. 大英博物馆. (2024). 有趣地探索博物馆。取自 https://www.britishmuseum.org/virtual-tour\n"
)
