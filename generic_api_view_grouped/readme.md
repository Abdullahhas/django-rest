Good question — this is core DRF design, not a mistake 👍
Let’s break it down clearly.

Short Answer

You write
queryset = Student.objects.all()

in each API view class because:

👉 Each view is independent, and DRF needs to know which data this specific view is allowed to work with.

What DRF uses queryset for

queryset is not for you, it’s for DRF internals.

DRF uses it to:

1: List records

self.list()

2: Retrieve single record

self.retrieve()


https://chatgpt.com/c/693d26b4-8e3c-8321-af12-62762df218a9

yaha se pr lo ke kio hm queryset = Student.objects.all() har dafa likh rahe hein
