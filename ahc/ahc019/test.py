import numpy as np
from scipy import ndimage

def rotate_shift_zero_largest_common(a, b):
    def rotate(matrix, axis, k):
        if axis == "x":
            return np.rot90(matrix, k=k, axes=(1, 2))
        elif axis == "y":
            return np.rot90(matrix, k=k, axes=(0, 2))
        elif axis == "z":
            return np.rot90(matrix, k=k, axes=(0, 1))
        else:
            raise ValueError("Invalid axis")

    def shift(matrix, axis, amount):
        return np.roll(matrix, shift=amount, axis=axis)

    def find_largest_connected_component(arr):
        structure = ndimage.generate_binary_structure(3, 1)
        labeled, num_features = ndimage.label(arr, structure=structure)
        sizes = ndimage.sum(arr, labeled, range(1, num_features + 1))
        if sizes.size == 0:
            return None, None
        largest_component_label = np.argmax(sizes) + 1
        return labeled == largest_component_label, largest_component_label, sizes[largest_component_label - 1]

    axes = ["x", "y", "z"]
    rotations = [0, 1, 2, 3]  # 0, 90, 180, 270 degrees
    shifts = [-2, -1, 0, 1, 2]
    largest_component = None
    largest_component_label = None
    largest_component_size = 0
    best_rotation = None
    best_shift = None

    for axis in axes:
        for k in rotations:
            a_rotated = rotate(a, axis, k)
            for axis_shift in range(3):  # x, y, z axes
                for shift_amount in shifts:
                    a_shifted = shift(a_rotated, axis_shift, shift_amount)
                    common_area = (a_shifted > 0) & (b > 0)
                    connected_component, component_label, component_size = find_largest_connected_component(common_area)
                    if connected_component is not None:
                        if component_size > largest_component_size:
                            largest_component_size = component_size
                            largest_component = connected_component
                            largest_component_label = component_label
                            best_rotation = (axis, k)
                            best_shift = (axis_shift, shift_amount)

    if largest_component is not None:
        a_rotated = rotate(a, best_rotation[0], best_rotation[1])
        a_shifted = shift(a_rotated, best_shift[0], best_shift[1])
        common_a_indices = np.where(largest_component)
        common_b_indices = np.where(largest_component)

        edited_values_a = set(a_shifted[common_a_indices])
        edited_values_b = set(b[common_b_indices])

        a_shifted[common_a_indices] = 0
        b[common_b_indices] = 0

        a = shift(a_shifted, best_shift[0], -best_shift[1])
        a = rotate(a, best_rotation[0], -best_rotation[1])

    return a, b, edited_values_a, edited_values_b, largest_component, largest_component_size

# 使用例:
a = np.random.randint(0, 3, (5, 5, 5))
b = np.random.randint(0, 3, (5, 5, 5))
print(a)
print(b)

a_zeroed, b_zeroed, edited_values_a, edited_values_b, largest_component, largest_component_size = rotate_shift_zero_largest_common(a, b)
print(a_zeroed)
print(b_zeroed)
print(edited_values_a)
print(edited_values_b)

print("Largest connected component:")
print(largest_component)
print(f"Largest connected component size: {largest_component_size}")
