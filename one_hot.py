import numpy as np
import setting

# NUMBER_LEN = len(setting.NUMBER)


# def encode(text):
#     vector = np.zeros(len(NUMBER_LEN * setting.MAX_CAPTCHA, dtype=float)
#     def char2pos(t):
#         for i, c in enumerate(setting.NUMBER):
#             if c == t:
#                 return i
#         raise ValueError('error')
#     for i, t in enumerate(text):
#         idx = i * NUMBER_LEN + char2pos(t)
#         vector[idx] = 1.0
#     return vector

def char2pos(t):
    for i, c in enumerate(setting.ALL_CHAR_SET):
        if c == t:
            return i
    print (t)
    raise ValueError('error')

def encode(text):
    vector = np.zeros(setting.ALL_CHAR_SET_LEN * setting.MAX_CAPTCHA, dtype=float)
    for i, t in enumerate(text):
        idx = i * setting.ALL_CHAR_SET_LEN + char2pos(t)
        vector[idx] = 1.0
    return vector

def decode(vec):
    char_pos = vec.nonzero()[0]
    text=[]
    for i, c in enumerate(char_pos):
        char = setting.ALL_CHAR_SET[c - (i * setting.ALL_CHAR_SET_LEN)]
        text.append(char)
    return "".join(text)

# if __name__ == '__main__':
#     e = encode("X")
#     print(e)
