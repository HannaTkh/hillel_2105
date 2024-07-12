
import logging

def log_event(username: str, status: str):

    log_message = f"Login event - Username: {username}, Status: {status}"

    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
    )
    logger = logging.getLogger("log_event")

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


# log_event('Garry', 'tgnft')
# @pytest.mark.parametrize('status', ['success', 'expired', 'third'])
# def test_success():
#     log_event('Anna', 'success')
#     assert True



