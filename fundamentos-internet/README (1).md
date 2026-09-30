# Internet Fundamentals

## 1. From Client to Server

![Diagram of the client-server flow: client, DNS, ISP router, HTTP/HTTPS, server, and status codes](file:///C:/Users/demer/Downloads/client-server-diagram.svg)

- **Client**: the device (or, more precisely, the software running on it, like the browser) from which information is requested.
- **DNS**: a translator, it tells the network which IP address corresponds to the domain you typed.
- **IP**: a label for each device. Private IPs (on your local network) don't leave the network; the ISP router's IP is public, because it needs to be reachable by any server in the world.
- **Server**: a machine built to store information and handle millions of requests per second, not for normal end-user use.
- **HTTP**: the protocol for sending and receiving *requests* (client-server calls). It includes the path and parameters that indicate what's being requested.
- **Methods** (GET, POST, PUT, DELETE): define the action performed on the resource.
- **HTTPS**: the same HTTP, but encrypted — more secure.
- **Status codes**: the result of the request, grouped in hundreds — 2xx success, 4xx your error, 5xx server error.


## 2. Frontend and Backend in Action

Frontend and backend are two separate programs that understand each other thanks to an **API**: the contract for what one can ask the other.

- **Frontend**: HTML, CSS, and JavaScript. It never connects directly to the database, it only requests data through the API.
- **Backend**: uses a variety of languages, frameworks, and databases; it's the one with direct access to the database.
- **Why they don't collapse between updates**: as long as the backend doesn't change the API contract, it can change everything internally without the frontend ever noticing.


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
- **Collection name:** First Collection
- **Requests added:**
  - GET - https://jsonplaceholder.typicode.com/posts/1/comments
  - POST - https://jsonplaceholder.typicode.com/posts
  - PUT/PATCH/DELETE - PUT to https://jsonplaceholder.typicode.com/posts/1



### 4.3 Execution and Analysis

| Request | Method | Endpoint | Status Code | Notes |
|---------|--------|----------|--------------|-------|
| Read a post's comments | GET | /posts/1/comments | 200 OK | Returns the array of comments for post 1 |
| Create resource | POST | /posts | 201 Created | Body was corrected: originally sent each field as a separate dictionary, fixed it into a single JSON object |
| Update resource | PUT | /posts/1 | 200 OK | Had to fix the test to check for `Content-Type: application/json; charset=utf-8` instead of `text/html` |

### 4.4 Technical Explanation

#### GET /posts/1/comments
- **HTTP Method:** GET
- **Endpoint:** https://jsonplaceholder.typicode.com/posts/1/comments
- **Parameters / body:** none
- **Response description:** `200 OK`, returns a JSON array with the comments for the post with id 1.

#### POST /posts
- **HTTP Method:** POST
- **Endpoint:** https://jsonplaceholder.typicode.com/posts
- **Parameters / body:**
```json
{
  "name": "Snoop Dog",
  "id": "102",
  "color": "Green"
}
```
- **Response description:** `201 Created`. The API simulates creating the resource and returns the same object sent. It isn't actually saved on the server.

#### PUT /posts/1
- **HTTP Method:** PUT
- **Endpoint:** https://jsonplaceholder.typicode.com/posts/1
- **Parameters / body:** corrected JSON object (same format as the POST, no longer making the mistake of sending each field as a separate dictionary)
- **Response description:** `200 OK`, with the header `Content-Type: application/json; charset=utf-8`.

**What did you learn from the process?**
I learned how broad and wildly varied the world of APIs is. Most use authentication to prevent pointless or malicious requests — even simple APIs, like recipe ones, required it, and I had to discard them for this exercise. Understanding how client-server requests work made me realize how much it matters to control who can make what request. Since I'm interested in cybersecurity, I tried looking for APIs that detect malicious, fake, or reported IPs, and it was impossible to find one without authentication that also had methods beyond GET. DELETE in particular is extremely rare to find open, and it makes sense: almost nobody who designs a public API wants just anyone to be able to delete things from their server.

### 4.5 Final Reflection
After this exercise, I feel much closer to understanding how the internet works than before. It's no longer a black box: I can see the full path, from the client asking for something to the server responding, and I understand why each layer of protection (authentication, data validation, status codes) exists for a concrete reason and not just because.
