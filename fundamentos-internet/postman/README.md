# Internet Fundamentals

## 1. From Client to Server

Diagram can be found in: client-server-diagram.jpg

Here's what happens, step by step, from the moment you type `www.youtube.com` until the video appears on screen:

1. **You type the URL — the client sends the first request.** The client is not just the device, it's the software running on it (the browser) that prepares and sends the request for `www.youtube.com`.
2. **DNS resolves the domain into an IP.** Before anything can be sent across the network, the browser needs an actual address to send it to. DNS acts as a translator: it tells the browser which IP address corresponds to `www.youtube.com`.
3. **The request leaves your network through your ISP router.** Your device has a private IP (not reachable from outside your network), so your router translates it into its own public IP via NAT — that public IP is what makes you reachable by any server in the world.
4. **A secure channel is negotiated — this is where HTTPS enters.** Before the actual HTTP request is sent, the client and the server perform a TLS handshake to encrypt the connection. HTTPS is simply HTTP traveling through that encrypted tunnel; only after the handshake completes does the browser send the real request (`GET /watch?v=...`).
5. **The server receives the request and looks up the video.** A server is a machine (really, a role — not a specific type of hardware) built to handle massive numbers of simultaneous requests, not to be used directly like a personal computer.
6. **The server sends back a response.** The response includes a status code plus the content — `200 OK` means success, and along with it comes the video data that starts playing in your browser.

## 2. Frontend and Backend in Action

Frontend and backend are two separate programs that understand each other thanks to an **API**: the contract for what one can ask the other. To make this concrete, here's how it plays out in a medical appointment booking app:

- **Frontend** (React, HTML, CSS): renders the calendar with available time slots and handles the interface — the patient clicks a slot, and the frontend sends the **request**.
- **Backend** (Node.js, Express, a database): receives that request, checks the database to confirm the slot is actually still free, and sends back the **response** — either a confirmation or a rejection.

**The flow in request/response terms**: when a patient picks a time, the frontend sends a request like `POST /appointments` with the chosen date and time. The backend validates it against the database and returns a response: a `201 Created` with the confirmed appointment, or something like `409 Conflict` if someone else just took that same slot. The frontend never touches the database directly — it only ever sees what the backend decides to send back in the response.

**Why they don't collapse between updates**: as long as the backend doesn't change the API contract (what an endpoint expects and what it returns), it can change everything internally — the framework, the database, the validation logic — without the frontend ever noticing.

## 3. REST vs SOAP vs GraphQL

| API Type | Data Format Used | Flexibility Level | Implementation Difficulty | Current Usage (High / Medium / Low) |
|----------|-------------------|--------------------|-----------------------------|----------------------------------------|
| REST     | JSON              | Medium             | Low                         | High                                   |
| SOAP     | XML               | Low                | High                        | Low                                    |
| GraphQL  | JSON              | High               | Medium                      | Medium                                 |

**Which one is most appropriate for a modern startup? Why?**
REST, because it's simple to implement, every developer already knows it, and it's more than enough for most use cases. GraphQL pays off when the app needs to request very specific and varied data (large apps with many screen types, for example), but it costs more to set up. SOAP is barely used today, except in legacy or heavily regulated systems (banking, government), because of how rigid and heavy it is.

## 4. Exploring APIs with Postman

### 4.1 API Selection
- **API name:** JSONPlaceholder
- **Description:** A fake REST API for testing, with no authentication, that simulates resources like posts, users, and comments. Write operations (POST, PUT, DELETE) don't actually persist on the server, but the response simulates as if they did.

### 4.2 Postman Setup
- **Collection name:** JSONPlaceholder-CRUD
- **Requests added:**
  - `GET - Get list of posts` → `https://jsonplaceholder.typicode.com/posts`
  - `POST - Create a new post` → `https://jsonplaceholder.typicode.com/posts`
  - `PUT - Update an existing post` → `https://jsonplaceholder.typicode.com/posts/1`


### 4.3 Execution and Analysis

| Request | Method | Endpoint | Status Code | Relevant Headers | Notes |
|---------|--------|----------|--------------|-------------------|-------|
| Get list of posts | GET | /posts | 200 OK | `content-type: application/json; charset=utf-8`, `cache-control: max-age=43200` | Returns the full array of 100 posts |
| Create a new post | POST | /posts | 201 Created | `content-type: application/json; charset=utf-8`, `location: https://jsonplaceholder.typicode.com/posts/101` | Body was corrected: originally sent each field as a separate dictionary, fixed it into a single JSON object |
| Update an existing post | PUT | /posts/1 | 200 OK | `content-type: application/json; charset=utf-8`, `cache-control: no-cache` | Had to fix the test to check for `Content-Type: application/json; charset=utf-8` instead of `text/html` |

### 4.4 Technical Explanation

#### GET - Get list of posts
- **HTTP Method:** GET
- **Endpoint:** https://jsonplaceholder.typicode.com/posts
- **Parameters / body:** none
- **Response description:** `200 OK`, returns a JSON array of all 100 posts in the fake database.

#### POST - Create a new post
- **HTTP Method:** POST
- **Endpoint:** https://jsonplaceholder.typicode.com/posts
- **Parameters / body:**
```json
{
  "title": "Testing post",
  "body": "This is my test:p",
  "userId": "04"
}
```
- **Response:**
```json
{
  "title": "Testing post",
  "body": "This is my test:p",
  "userId": "04",
  "id": 101
}
```
- **Response description:** `201 Created`. I didn't send an `id` in the body, and the API assigned `101` on its own — one more than the 100 posts that already existed. That's the server's job, not something the client should decide.

#### PUT - Update an existing post
- **HTTP Method:** PUT
- **Endpoint:** https://jsonplaceholder.typicode.com/posts/1
- **Parameters / body:**
```json
{
  "id": 420,
  "title": "Updating post",
  "body": "Primer body... bueno en realidad 2do",
  "userId": "Caldosa01"
}
```
- **Response:**
```json
{
  "id": 1,
  "title": "Updating post",
  "body": "Primer body... bueno en realidad 2do",
  "userId": "Caldosa01"
}
```
- **Response description:** `200 OK`. Even though I sent `"id": 420` in the body, the response came back with `"id": 1` — the id in the URL path (`/posts/1`) is what actually identifies the resource, and the API ignored the id I tried to send in the body.

**What did you learn from the process?**
I learned how broad and wildly varied the world of APIs is. Most use authentication to prevent pointless or malicious requests — even simple APIs, like recipe ones, required it, and I had to discard them for this exercise. Understanding how client-server requests work made me realize how much it matters to control who can make what request. Since I'm interested in cybersecurity, I tried looking for APIs that detect malicious, fake, or reported IPs, and it was impossible to find one without authentication that also had methods beyond GET. DELETE in particular is extremely rare to find open, and it makes sense: almost nobody who designs a public API wants just anyone to be able to delete things from their server.

### 4.5 Final Reflection
After this exercise, I feel much closer to understanding how the internet works than before. It's no longer a black box: I can see the full path, from the client asking for something to the server responding, and I understand why each layer of protection (authentication, data validation, status codes) exists for a concrete reason and not just because.
