#include <iostream>
#include "Array.h"
#include <sys/time.h>
typedef struct
{
    int f, s;
}at;
int cmp(at a, at b)
{
    return a.f - b.f;
}
std::ostream& operator<<(std::ostream& os, at elem)
{
    std::cout << "{ " << elem.f << ", " << elem.s << "} ";
    return os;
}
int main() {
    at c{1, 2};
    Array<at> a(12, c);
    for (size_t i = 0; i < a.getLength(); i++)
        a[i] = at{rand() % 9, rand() % 12};
    std::cout << a << std::endl;
    a.qsort(cmp);
    std::cout << a << std::endl;
    return 0;
}
