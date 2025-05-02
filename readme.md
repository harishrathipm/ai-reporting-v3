# AI Reporting Application

## Frontend Overview

The frontend of this application is built using React and Material-UI. It is designed to dynamically render responses from the backend in various formats, such as chat, tables, images, charts, and more. The frontend is located in the `frontend/` directory and includes the following key components:

### Components

1. **Chat Component** (`Chat.jsx`):

   - Displays a chat interface for user interaction.

2. **Paginated Table Component** (`PaginatedTable.jsx`):

   - Renders tabular data with pagination support.

3. **Image Renderer Component** (`ImageRenderer.jsx`):

   - Displays images in the response.

4. **Plain Text Renderer Component** (`PlainTextRenderer.jsx`):

   - Renders plain text responses.

5. **Chart Renderer Component** (`ChartRenderer.jsx`):

   - Visualizes data in chart formats (e.g., bar, line, pie).

6. **Error Message Component** (`ErrorMessage.jsx`):

   - Displays error messages when something goes wrong.

7. **Loading Spinner Component** (`LoadingSpinner.jsx`):

   - Shows a loading indicator while waiting for responses.

8. **Card Renderer Component** (`CardRenderer.jsx`):

   - Displays summarized data in a card format.

9. **Response Renderer Component** (`ResponseRenderer.jsx`):
   - Dynamically selects and renders the appropriate component based on the response type.

### Testing the Components

Each component has corresponding test files (e.g., `PaginatedTable.test.jsx`) to ensure functionality. Tests are written using `@testing-library/react`.

## Example Prompts to Test Components

To test the components, you can use the `/chat` API with the following example prompts:

1. **Chat Component**:

   - Prompt: "What is the capital of France?"
   - Expected Response: A plain text message like "The capital of France is Paris."

2. **Paginated Table Component**:

   - Prompt: "Show me a table of the top 5 programming languages by popularity."
   - Expected Response: A table with columns like "Language" and "Popularity" and 5 rows of data.

3. **Image Renderer Component**:

   - Prompt: "Show me an image of the Eiffel Tower."
   - Expected Response: An image URL rendered in the frontend.

4. **Plain Text Renderer Component**:

   - Prompt: "Explain the concept of machine learning."
   - Expected Response: A detailed plain text explanation.

5. **Chart Renderer Component**:

   - Prompt: "Show me a bar chart of sales data for the last 3 months."
   - Expected Response: A bar chart with sales data.

6. **Error Message Component**:

   - Prompt: "Trigger an error."
   - Expected Response: An error message displayed in the frontend.

7. **Loading Spinner Component**:

   - Prompt: "Simulate a delayed response."
   - Expected Response: A loading spinner displayed until the response is received.

8. **Card Renderer Component**:
   - Prompt: "Summarize the latest news in a card format."
   - Expected Response: A card with a title and summary of the news.

## Running the Frontend

To run the frontend locally:

1. Navigate to the `frontend/` directory.
2. Install dependencies: `npm install`
3. Start the development server: `npm start`

The application will be available at `http://localhost:3000` by default.

## Running Tests

To run the tests for the frontend:

1. Navigate to the `frontend/` directory.
2. Run the tests: `npm test`

This will execute all test cases and display the results in the terminal.

## Coding Practices for the React App

To ensure maintainability, scalability, and readability of the React application, follow these best practices:

### 1. **Component Structure**

- Use functional components with React hooks instead of class components.
- Keep components small and focused on a single responsibility.
- Use a `components/` directory to organize reusable components.
- Use a `pages/` directory for page-level components if applicable.

### 2. **Styling**

- Use Material-UI for consistent and modern styling.
- Prefer `sx` prop or `makeStyles` for styling over inline styles.
- Avoid hardcoding styles; use theme variables for consistency.

### 3. **State Management**

- Use React's `useState` and `useReducer` for local component state.
- Use `Context API` or libraries like `Redux` for global state management if needed.
- Avoid prop drilling by lifting state up or using context.

### 4. **Code Organization**

- Group related files together (e.g., component, styles, and tests in the same folder).
- Use meaningful and consistent naming conventions for files and variables.
- Separate concerns by keeping logic, UI, and API calls in different layers.

### 5. **Testing**

- Write unit tests for all components using `@testing-library/react`.
- Ensure tests cover edge cases and user interactions.
- Use mock data for testing API calls.

### 6. **Error Handling**

- Handle errors gracefully in components and display user-friendly messages.
- Use `ErrorBoundary` for catching errors in React components.
- Log errors to the console or a monitoring service for debugging.

### 7. **Performance Optimization**

- Use `React.memo` for memoizing components to prevent unnecessary re-renders.
- Use `useCallback` and `useMemo` hooks to optimize expensive computations.
- Lazy load components using `React.lazy` and `Suspense`.

### 8. **API Integration**

- Use a dedicated API client (e.g., `ApiClient.js`) for making HTTP requests.
- Keep API calls out of components; use custom hooks (e.g., `useFetch`) for data fetching.
- Handle loading and error states for API calls.

By following these practices, the React app will remain clean, maintainable, and scalable as it grows.
