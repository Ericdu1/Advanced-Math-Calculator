import numpy as np

def add_matrices(A, B):
    """ 矩阵加法 """
    try:
        return np.add(A, B)
    except ValueError:
        return "错误: 矩阵维度不匹配，无法相加"

def multiply_matrices(A, B):
    """ 矩阵乘法 """
    try:
        return np.dot(A, B)
    except ValueError:
        return "错误: 矩阵维度不匹配，无法相乘"

def transpose_matrix(A):
    """ 矩阵转置 """
    return np.transpose(A)

def determinant(A):
    """ 计算矩阵行列式 """
    if A.shape[0] != A.shape[1]:
        return "错误: 计算行列式需要方阵"
    return np.linalg.det(A)

def inverse_matrix(A):
    """ 计算矩阵的逆 """
    if A.shape[0] != A.shape[1]:
        return "错误: 逆矩阵需要方阵"
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "错误: 该矩阵不可逆（行列式为0）"

def format_matrix(A):
    """ 格式化矩阵，让它以单行字符串输出，避免换行错位 """
    if isinstance(A, str):  # 错误信息直接返回
        return A
    return "\n".join([" ".join(f"{num:.2f}" for num in row) for row in A])
