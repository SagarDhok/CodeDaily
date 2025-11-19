

#! 929. Unique Email Addresses
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            unique_emails.add(local + '@' + domain)
        return len(unique_emails)

# Example usage
sol = Solution()
print(sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))  
print(sol.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))  
