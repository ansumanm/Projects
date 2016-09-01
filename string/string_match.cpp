#include<string>
#include<iostream>

using namespace std;

/* Returns 0 if match not found. */
/* Returns location if match found. */

bool stringMatchBruteForce(string &s,string &p)
{
	string::const_iterator s_i;
	string::const_iterator p_i;

	for(s_i = s.begin();s_i != s.end(); s_i++)
	{
		p_i = p.begin();
		// cout << "Debug #1 *s_i " << *s_i << " *p_i " << *p_i << endl; 

		while(*p_i != *s_i) 
		{
			s_i++;
			// cout << "Debug #2 *s_i " << *s_i << " *p_i " << *p_i << endl; 
			if (s_i == s.end())
			{
				// cout << "Debug #3" << endl; 
				return false;
			}
		}

		// First character match found. 
		// Now compare the rest of the characters.
		string::const_iterator s_i_2;
		string::const_iterator p_i_2;

		s_i_2 = s_i;
		p_i_2 = p_i;
		// cout << "Debug #4 *s_i_2 " << *s_i_2 << " *p_i_2 " << *p_i_2 << endl; 

		do {
			s_i_2++;
			p_i_2++;

			// cout << "Debug #5 *s_i_2 " << *s_i_2 << " *p_i_2 " << *p_i_2 << endl; 
			if (p_i_2 == p.end())
			{
				// cout << "Debug #6" << endl; 
				return true;
			}

			if (s_i_2 == s.end())
			{
				// cout << "Debug #7" << endl; 
				return false;
			}
		} while(*s_i_2 == *p_i_2);
	}
	/ cout << "Debug #8" << endl; 
	return false;
}

int main()
{
	string ss = "A quick brown fox jumps over the lazy dog";
	string p = "lazy";
	bool matchFound;

	matchFound = stringMatchBruteForce(ss,p);

	cout << (matchFound ? "Match found" : "Match not found");
	cout << endl;

	string q = "crazy";
	matchFound = stringMatchBruteForce(ss,q);

	cout << (matchFound ? "Match found" : "Match not found");
	cout << endl;

	return 0;
}
