package main

import "fmt"

func main() {
    fmt.Printf("sum of 5 and 5 is %v \n",Sum(5, 5))
}


func Sum(x int, y int) int {
    return x + y
}

