#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int process_instructions(const vector<string> &instructions)
{
    int current = 50;
    int zero_count = 0;

    for (const string &instruction : instructions)
    {
        char direction = instruction[0];
        int steps = stoi(instruction.substr(1)); // convert everything after the direction to an int

        // turning left
        if (direction == 'L')
        {
            int to_zero = current;

            // Check if we will reach zero
            if (steps >= to_zero && to_zero > 0)
            {
                zero_count++;
                steps -= to_zero;
                current = 0;
            }

            // Count how many times we can fully wrap back around to zero
            while (steps >= 100)
            {
                zero_count++;
                steps -= 100;
            }

            // final position
            current = (current - steps) % 100;
            if (current < 0)
                current += 100; // extra step for negative modulo in C++
        }
        // turning right
        else if (direction == 'R')
        {
            int to_zero = (100 - current) % 100;

            // Check if we are going to reach zero (and aren't starting at 0)
            if (steps >= to_zero && to_zero > 0)
            {
                zero_count++;
                steps -= to_zero;
                current = 0;
            }

            // Count how many times we can fully wrap around to zero
            while (steps >= 100)
            {
                zero_count++;
                steps -= 100;
            }

            // Final position
            current = (current + steps) % 100;
        }
    }

    return zero_count;
}

int main()
{
    ifstream file("../input/day1_input");
    vector<string> instructions;
    string line;

    while (getline(file, line))
    {
        if (!line.empty())
        {
            instructions.push_back(line);
        }
    }
    file.close();

    int password = process_instructions(instructions);
    cout << password << endl;

    return 0;
}