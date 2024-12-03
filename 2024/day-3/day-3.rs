// Solution 1:
// grep -Po 'mul\((\d{1,3}),(\d{1,3})\)' input.txt > parsed-input.txt
// sed -i -e 's/mul(//g' parsed-input.txt
// sed -i -e 's/)//g' parsed-input.txt
// sed -i -e 's/,/ /g' parsed-input.txt
//
// solution 2:
// grep -Po "(mul\\((\\d+),(\\d+)\\))|(do\\(\\))|(don't\\(\\))" input.txt.bak > parsed-input2.txt
// repeat 'sed' steps from lines 2,3,4
// sed -i -e 's/(//g' parsed-input.txt
//
// could've made a bash script for this whole thing, but honestly, couldn't be arsed.

use std::fs::File;
use std::io::{prelude::*, BufReader};

fn main() {
    let file = File::open("parsed-input2.txt").unwrap();
    let reader = BufReader::new(file);
    let mut sum = 0;
    let mut dont = false;

    for line in reader.lines() {
        let line = line.unwrap();
        if line == "don't" {
            dont = true;
            continue;
        } else if line == "do" {
            dont = false;
            continue;
        }

        if !dont {
        let parts = line.split(" ");
        let mut product: i32 = 1;
        for part in parts {
            product *= part.parse::<i32>().unwrap();
        }
        sum += product;
        }
    }

    println!("answer: {}", sum);

}
