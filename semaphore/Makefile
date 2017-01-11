all: p1 p2

p1: p1.c
	gcc p1.c -lpthread -o p1

p2: p2.c
	gcc p2.c -lpthread -o p2

clean:
	rm -f p1
	rm -f p2

.PHONY: p1 p2

