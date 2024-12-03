// grep -Po 'mul\((\d{1,3}),(\d{1,3})\)' input.txt > parsed-input.txt
// sed -i -e 's/mul(//g' parsed-input.txt
// sed -i -e 's/)//g' parsed-input.txt
// sed -i -e 's/,/ /g' parsed-input.txt

use std::fs::File;
use std::io::{prelude::*, BufReader};

fn main() {
    let file = File::open("parsed-input.txt").unwrap();
    let reader = BufReader::new(file);
    let mut sum = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        let parts = line.split(" ");
        let mut product: i32 = 1;
        for part in parts {
            product *= part.parse::<i32>().unwrap();
        }
        sum += product;
    }

    println!("answer 1: {}", sum);

}
