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
    "## 大英博物館簡介\n"
    "大英博物館位於英國倫敦布魯姆斯伯里，是世界上最大、最重要的人類歷史文化博物館之一。該博物館成立於 1753 年，是第一個公共國家博物館，以漢斯·斯隆爵士的藏品為基礎建立。博物館於 1759 年向公眾開放，現已發展成為一流的文化機構 [1]。\n\n"
    "## 位置和建築\n"
    "博物館位於大羅素街，可透過倫敦的幾個地鐵站輕鬆抵達。其標誌性的大庭院由福斯特建築事務所設計，是其顯著的建築特色，為遊客提供了寬敞的探索環境。博物館位於布魯姆斯伯里，使其成為倫敦文化活動的中心樞紐 [2]。\n\n"
    "## 收藏規模和意義\n"
    "大英博物館收藏了超過 800 萬件藏品，記錄了人類文化從起源到現在的歷史。這個龐大的收藏品包括羅塞塔石碑和埃爾金大理石雕等文物。這些物品不僅具有重要的歷史價值，還具有重要的文化和教育意義。該藏品跨越了 200 多萬年的人類歷史，是世界上最全面的藏品之一 [3]。\n\n"
    "## 訪客數量\n"
    "近年來，大英博物館一直是英國遊客最多的景點之一。 2024年，它將接待約650萬遊客，較前幾年大幅成長。如此高的參觀人數歸功於其引人入勝的展覽及其作為文化偶像的地位 [4]。\n\n"
    "## 近期值得關注的展覽\n"
    "最近的展覽包括“軍團：羅馬軍隊的生活”和“米開朗基羅：最後幾十年”，這些展覽特別受遊客歡迎[1]。這些展覽凸顯了博物館策劃吸引廣泛觀眾的引人入勝且具有教育意義的展覽的能力。此外，博物館的臨時展覽經常展出來自世界各地的文物，展示其全球影響力[4]。\n\n"
)

# Content for high information completeness
LOW_INFO_CONTENT = (
    "## 大英博物館簡介\n"
    "大英博物館是位於倫敦的著名機構。它建立已久，有很多有趣的東西可以看。博物館很大，每年都有很多遊客。它以漢斯·斯隆爵士的收藏為基礎建立，其中包括來自世界各地的各種物品 [1]。\n\n"
    "## 位置和建築\n"
    "博物館位於倫敦一個美麗的地區，名叫布魯姆斯伯里。它有一個非常令人印象深刻的大庭院。人們喜歡參觀，因為這裡交通便利，而且景色優美。博物館的地理位置使其成為遊客和當地人的熱門目的地 [2]。\n\n"
    "## 收藏規模和意義\n"
    "大英博物館有很多東西，包括一些著名的東西。雖然沒有全部展出，但展出的內容非常有趣。博物館對於了解歷史和文化很重要。它的藏品十分豐富，跨越了人類多年的歷史 [3]。\n\n"
    "## 訪客數量\n"
    "每年都有很多人參觀大英博物館。 2024年，遊客數量相當可觀，比前幾年增加。博物館總是很忙，尤其是在假日和夏季[4]。\n\n"
    "## 近期值得關注的展覽\n"
    "博物館最近舉辦了一些不錯的展覽。它們總是在變化，所以總是會有一些新的東西可以看。人們似乎很喜歡它們，它們也使博物館成為了一個受歡迎的目的地[1]。博物館也舉辦各種活動，為遊客帶來樂趣。此外，博物館的咖啡館也很不錯，為那些需要休息一下的遊客提供各種小吃和飲料。禮品店也值得一去，有許多獨特的物品可供購買 [4]。\n\n"
)

# References for low information source quality
LOW_SOURCE_REFS = (
    "References:\n"
    "1. Johnson, A. (2024). My Awesome Trip to The British Museum! Retrieved from https://peterblog.com\n"
    "2. Terry, B (2024). Best Places to Visit in London? Sharing with You. Retrieved from https://travel/%22z5few6y5%.com\n"
    "3. Claudia, C (2024). All you need to know about The British Museum. Retrieved from https://www.tripadvisor.co.uk/BritishMuseum.html\n"
    "4. Wilson, K. (2023). Top 10 Things to Do in The British Museum [Video]. YouTube. Retrieved from https://www.youtube.com/watch?v=example\n\n"
)

# References for high information source quality
HIGH_SOURCE_REFS = (
    "References:\n"
    "1. Johnson, A. (2024). My Awesome Trip to The British Museum! Retrieved from https://peterblog.com\n"
    "2. Terry, B (2024). Best Places to Visit in London? Sharing with You. Retrieved from https://travel/%22z5few6y5%.com\n"
    "3. Claudia, C (2024). All you need to know about The British Museum. Retrieved from https://www.tripadvisor.co.uk/BritishMuseum.html\n"
    "4. Wilson, K. (2023). Top 10 Things to Do in The British Museum [Video]. YouTube. Retrieved from https://www.youtube.com/watch?v=example\n\n"
)
