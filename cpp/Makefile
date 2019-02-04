CC=g++
CFLAGS=-std=c++11 -O3 -Wall

build: vc_validate.cpp
	$(CC) $(CFLAGS) vc_validate.cpp -o vc_validate

verbose: vc_validate.cpp
	$(CC) $(CFLAGS) -D VERBOSE vc_validate.cpp -o vc_validate

clean: vc_validate
	rm vc_validate
	