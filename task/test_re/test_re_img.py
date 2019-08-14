import re


def test_re_img():
    # 读取html
    # 默认是读的模式
    with open("img.html", encoding="utf-8") as f:
        html = f.read()
        print(html)
    p = re.compile(r"<img.+?src=\"(.+?)\".+?>")
    img_list = p.findall(html)
    """
    findall函数，在正则匹配里，当正则没有分组，返回就是正则匹配；如果有分组，就仅仅匹配分组里面的内容，
    然后返回这个组的列表；如果有多个分组，会把每一个分组看成一个单位，组合为一个元组，然后返回一个含有多个元组的列表。
    """
    print(len(img_list))
    for i in img_list:
        print(i.replace("&amp;", "&"))


if __name__ == "__main__":
    test_re_img()
