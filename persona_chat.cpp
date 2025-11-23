#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <random>
#include <unordered_map>

using namespace std;

vector<string> load_examples(const string& path) {
    ifstream in(path);
    vector<string> lines;
    string line;
    while (getline(in, line)) {
        if (!line.empty()) lines.push_back(line);
    }
    return lines;
}

// Very small Markov-ish generator (toy). Replace with real LLM call in production.
string generate_reply(const vector<string>& examples, const string& user) {
    if (examples.empty()) return "I'm here—tell me more.";
    static random_device rd;
    static mt19937 gen(rd());
    uniform_int_distribution<size_t> dist(0, examples.size() - 1);

    // Pick a reference line and echo part of the user prompt
    string ref = examples[dist(gen)];
    if (ref.size() > 120) ref = ref.substr(0, 120) + "...";
    string user_short = user.size() > 60 ? user.substr(0, 60) + "..." : user;
    return "Thinking like: \"" + ref + "\" — I hear you about \"" + user_short + "\".";
}

int main() {
    auto examples = load_examples("reference_samples.txt");
    cout << "Persona chat (toy). Type 'quit' to exit.\n";
    string user;
    while (true) {
        cout << "You: ";
        if (!getline(cin, user)) break;
        if (user == "quit" || user == "exit") break;
        string reply = generate_reply(examples, user);
        cout << "AI: " << reply << "\n";
    }
    return 0;
}
