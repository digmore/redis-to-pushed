# redis-to-pushed
Subscribe to a Redis channel, saving messages received through it to a single Pushed.co account

# What is redis-to-pushed?

redis-to-pushed is a Python application which will subscribe to a Redis
channel, posting messages received through the channel to a single Pushed.co account.

# How to use this image

This redis-to-pushed container must be linked to a
[redis](https://hub.docker.com/_/redis/) container (which must have the alias
`redis`). Pushed.co application credentials must be supplied as environment variables. 

    docker run --name redis-to-pushed --link redis:redis -e APP_KEY='YOUR_APP_KEY' -e APP_SECRET='YOUR_APP_SECRET' -e PUSHED_ID='YOUR_PUSHED_ID' -d digmore/redis-to-pushed

**NOTE**: The default channel name is `notifications`. See the `CHANNEL` environment variable below to override this.

## Configuration

ENVIRONMENT VARIABLES (only available with `docker run`)

 * `APP_KEY` - The app key for your Pushed.co application (required)
 * `APP_SECRET` - The app secret for your Pushed.co application (required)
 * `PUSHED_ID` - Specify the Pushed ID of a single Pushed.co account (required)
 * `CHANNEL` - Set the Redis channel name to subscribe to (optional, defaults to `pushed`)

# User Feedback

## Issues

If you want to contact me with questions, or to report problems with this image,
please raise a [GitHub issue](https://github.com/digmore/redis-to-pushed/issues)

