# Mission 7 — How computers communicate

## 1. Task / objective
Explain basic network types and concepts, observe a connectivity test and a DNS lookup from Terminal, and describe what happens when a website opens.

## 2. Work completed

### Task 7.1 — Network concepts

| Concept | My explanation | Example |
|---|---|---|
| LAN | A network covering a small area, such as a home, lab or office, joining the devices there | My laptop, phone and router on my home Wi-Fi |
| MAN | A network covering a city or large campus area, linking many LANs together | A city-wide network connecting government buildings |
| WAN | A network covering large geographical areas; the widest network of networks | The internet itself, carrying traffic between countries |
| DNS | The directory service that translates a domain name into the IP address machines actually use | Looking up `example.org` and receiving its address |
| Router | A device that connects networks and forwards data between them, choosing which way each packet goes | My home router passing my traffic from the LAN to my internet provider |
| Protocol | An agreed set of rules devices follow so they can understand each other | HTTP/HTTPS between a browser and a website |
| Packet switching | Data is split into packets that travel independently across the network and are reassembled at the destination | Parts of a video call taking slightly different routes yet arriving together |
| Client-server | A client requests a service and a server provides it | My browser (client) asking GitHub (server) for a page |

### Task 7.2 — Network observations (privacy-safe)
- **Connectivity test:** `ping -c 4 example.com` sent four small test packets to example.com and received four replies (0% loss, ~20–26 ms each). The example.com name was resolved to the public address 104.20.23.154. A connectivity test checks whether my computer can actually reach a destination at all — if it fails, the problem is in my network path, not in the website.
- **DNS lookup:** `nslookup example.org` asked the DNS system for example.org's address and displayed the public answer (the local resolver's address was redacted from my evidence). A DNS lookup displays the name it queried and the IP address(es) that name maps to.
- **Role of DNS:** when I type a website name, my machine does not know where that site lives; DNS answers the question "what IP address belongs to this name?" so the browser then knows which machine to talk to.

### Task 7.3 — What happens when I open a website

1. The **client** (my browser) receives the address I typed, e.g. `https://example.org`, and first needs the site's IP address.
2. The browser asks **DNS**, which looks up the name and replies with the server's IP address.
3. My request leaves the computer through my home network (LAN) and the **router**, which forwards it across the wider network toward that address.
4. The request follows the rules of the **protocol** (HTTPS) and arrives at the **server** hosting example.org.
5. The server processes the request and sends a response back — the page's files — as data packets.
6. The packets are reassembled on my side and the browser reads them and displays the page to me.

## 3. Commands / tools used
`ping -c 4` (connectivity test measuring reachability and round-trip time), `nslookup` (DNS lookup showing the address a domain maps to).

## 4. My understanding
Networks are layers of scope — LAN is my room, MAN is my city, WAN is the world — and routers are the junctions between those scopes. Names are for humans, addresses are for machines, and DNS is the translation step between the two. Seeing ping measure 20-odd millisecond round-trip times made "packet switching" concrete: data really does make timed physical journeys, and protocols are what let both ends agree on what each packet means.

## 5. Difficulties faced
The nslookup output initially included my local DNS resolver's address, which is identifying network information I should not publish.

## 6. How I resolved them
Redacted the resolver/server lines from the saved evidence and kept only the public query and answer, as the assignment requires.

## 7. Evidence / files
- `evidence/mission-07/network-observations.txt` — ping results and DNS lookup output (personal network details redacted).

## 8. Commit details
Commit message: `Explain networking concepts and website communication` — committed and pushed to GitHub.
