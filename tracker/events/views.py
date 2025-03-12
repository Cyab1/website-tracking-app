# Import necessary modules and libraries
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Event
from datetime import datetime
import logging

# Set up logging to help with debugging and monitoring
logger = logging.getLogger(__name__)


# Define the home view to render the main page
def home(request):
    """
    Renders the home page of the application.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered HTML page.
    """
    return render(request, "events/index.html")


# Define the track_event view to handle event tracking
@csrf_exempt  # Disable CSRF protection for simplicity (consider adding security later)
def track_event(request):
    """
    Handles POST requests to track events and save them to the database.

    Args:
        request (HttpRequest): The request object containing event data.

    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """
    if request.method == "POST":
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            logger.info(
                "Received data: %s", data
            )  # Log the incoming data for debugging

            # Create a new Event object in the database using the received data
            Event.objects.create(
                event_type=data.get(
                    "event_type", "unknown"
                ),  # Default to "unknown" if not provided
                timestamp=datetime.fromisoformat(
                    data["timestamp"]
                ),  # Convert ISO format to datetime
                url=data.get("url", ""),  # Default to empty string if not provided
                user_agent=data.get(
                    "user_agent", ""
                ),  # Default to empty string if not provided
                element=data.get(
                    "element", ""
                ),  # Default to empty string if not provided
                element_id=data.get(
                    "id", ""
                ),  # Default to empty string if not provided
                duration=data.get("duration"),  # No default value, can be None
            )

            # Return a success response with a 201 status code
            return JsonResponse({"message": "Event tracked successfully"}, status=201)

        except KeyError as e:
            # Handle missing required fields in the request data
            logger.error("Missing required field: %s", str(e))  # Log the error
            return JsonResponse(
                {"error": f"Missing required field: {str(e)}"}, status=400
            )

        except ValueError as e:
            # Handle invalid data format (e.g., incorrect timestamp format)
            logger.error("Invalid data format: %s", str(e))  # Log the error
            return JsonResponse({"error": f"Invalid data format: {str(e)}"}, status=400)

    # Handle invalid request methods (e.g., GET, PUT, DELETE)
    return JsonResponse({"error": "Invalid request method"}, status=405)
