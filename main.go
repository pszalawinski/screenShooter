package main

import (
	"bufio"
	"fmt"
	"image"
	"image/png"
	"os"
	"time"

	"github.com/kbinani/screenshot"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Provide : ")

	scanner.Scan()

	var inputPath string = scanner.Text()
	if inputPath == "1" {
		captureDisplay(1)
	}
	if inputPath == "2" {
		captureDisplay(2)
	}

}

// func printerOne() {
// 	fmt.Println("kliknieto jeden")
// }

// func printerTwo() {
// 	fmt.Println("kliknieto dwa")
// }

func captureDisplay(i int) {

	bounds := screenshot.GetDisplayBounds(i)

	img, err := screenshot.CaptureRect(bounds)
	if err != nil {
		panic(err)
	}
	t := time.Now().Second()
	fileName := fmt.Sprintf("%d_time-%d.png", i, t)
	save(img, fileName)
	//fmt.Printf("#%d : %v \"%s\"\n", i, bounds, fileName)
}

func save(img *image.RGBA, filePath string) {
	file, err := os.Create(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	png.Encode(file, img)
}
