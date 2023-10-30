from Matrix import Matrix
from Stack import Stack
from Queue import Queue


def main():
    # 1
    my_stack = Stack()
    my_stack.push(5)
    # my_stack.push(7)
    print(my_stack.pop())
    print(my_stack.peek())

    # 2
    my_queue = Queue()
    my_queue.push(55)
    my_queue.push(77)
    print(my_queue.pop())
    print(my_queue.peek())

    # 3
    my_matrix = Matrix(2, 2)
    my_matrix.set_element(0, 0, 2)
    my_matrix.set_element(0, 1, 3)
    my_matrix.set_element(1, 0, 4)
    my_matrix.set_element(1, 1, 5)
    print(my_matrix.get_element(0, 0))
    print(my_matrix.transpose())
    print(my_matrix.multi_matrix([[1, 2], [3, 4]]))
    my_matrix.apply_operation(lambda x: 2 * x)


if __name__ == "__main__":
    main()
