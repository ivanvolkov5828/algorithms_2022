class QueueClass:
    def __init__(self):
        self.base = []
        self.solved = []
        self.revision = []

    def is_empty(self):
        return self.base == []

    def to_queue(self, el):
        self.base.insert(0, el)

    def from_queue(self):
        return self.base.pop()

    def to_solved(self):
        self.solved.insert(0, self.base.pop())

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def return_from_revision_to_base(self):
        self.base.insert(0, self.revision.pop())

    def size(self):
        return len(self.base)


if __name__ == '__main__':
    qc_obj = QueueClass()

    qc_obj.to_queue('first')
    qc_obj.to_queue('second')
    qc_obj.to_queue('third')

    print(qc_obj.base)

    qc_obj.to_solved()
    print(qc_obj.solved)

    qc_obj.to_revision()
    print(qc_obj.base)
    print(qc_obj.revision)

    qc_obj.return_from_revision_to_base()
    print(qc_obj.revision)
    print(qc_obj.base)