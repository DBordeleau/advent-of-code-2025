#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<long long> count_invalid_ids(const vector<string> &ranges)
{
    vector<long long> invalid_ids;

    for (const string &range : ranges)
    {
        long long start, end;
        char dash;

        stringstream ss(range);

        ss >> start >> dash >> end;

        // cout << range << endl;
        // cout << start << "-" << end << endl;

        while (start <= end)
        {
            string num_string = to_string(start);
            char first = num_string[0];
            if (first == '0')
            {
                invalid_ids.push_back(start);
                start++;
                continue;
            }

            string double_string = num_string + num_string;
            double_string.erase(0, 1); // remove first char
            double_string.pop_back();  // remove last char

            if (double_string.find(num_string) != string::npos)
            {
                invalid_ids.push_back(start);
                start++;
                continue;
            }
            start++;
        }
    }
    return invalid_ids;
}

int main()
{
    ifstream file("../input/day2_input");
    stringstream buffer;
    vector<string> ranges;

    buffer << file.rdbuf();
    string input_string = buffer.str();

    stringstream input_stream(input_string);
    string range;

    // Separate each range by comma and add to range vector
    while (getline(input_stream, range, ','))
    {
        ranges.push_back(range);
    }

    file.close();

    vector<long long> invalid_ids = count_invalid_ids(ranges);

    long long sum = 0;

    for (long long num : invalid_ids)
    {
        sum += num;
    }

    cout << "Answer: " << sum << endl;

    return 0;
}