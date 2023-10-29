from Stack import Stack
from Queue import Queue


def main():
    my_stack = Stack()
    my_stack.push(5)
    # my_stack.push(7)
    print(my_stack.pop())
    print(my_stack.peek())

    my_queue = Queue()
    my_queue.push(55)
    my_queue.push(77)
    print(my_queue.pop())
    print(my_queue.peek())


if __name__ == "__main__":
    main()
