# DNS — Fundamentals and Name Resolution

## 1. What Is DNS?

**DNS (Domain Name System)** helps translate human-readable domain names into DNS records, commonly including IP addresses used to locate services.

For example, people can remember `example.com` more easily than an IP address. DNS lets a client look up the information associated with that name.

Think of DNS as an internet contact book:

- **Name:** `example.com`
- **Lookup:** a DNS query
- **Result:** a DNS record, such as an IP address

DNS does not deliver the website itself. It helps the client discover where to connect.

## 2. Domain Name Hierarchy

Consider the domain `admin.tryhackme.com`. Its labels form a hierarchy, read from right to left:

- `.com` — Top-Level Domain (TLD)
- `tryhackme` — second-level domain
- `admin` — subdomain

A domain can contain multiple levels of subdomains. Each label is separated by a dot.

Common TLD categories include:

- **gTLD:** generic TLDs, such as `.com` and `.org`
- **ccTLD:** country-code TLDs, such as `.in` and `.uk`

This hierarchy helps DNS organize names and delegate responsibility for them.

## 3. Common DNS Record Types

DNS records store different kinds of information.

| Record | Purpose |
|---|---|
| `A` | Maps a name to an IPv4 address |
| `AAAA` | Maps a name to an IPv6 address |
| `CNAME` | Makes one name an alias of another name |
| `MX` | Identifies mail servers for a domain, with a priority value |
| `TXT` | Stores text used for verification and policies, among other purposes |

Example record:

```text
example.com.  300  IN  A  192.0.2.10
```

- `example.com` is the queried name.
- `300` is the TTL, in seconds.
- `A` is the record type.
- `192.0.2.10` is the IPv4 address.

The IP address above is an example address, not a claim about the real website.

**Remember:** A domain does not have to publish every record type. A missing `MX` record, for example, does not automatically mean its website's DNS is broken.
