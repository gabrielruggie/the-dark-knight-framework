from main.pending_payment_consumer import StripePendingPaymentConsumer
from main.completed_payment_consumer import StripeCompletedPaymentConsumer

from mock import patch
import redis

@patch("main.config.cache_connection.connection.set")
def test_cache_set_called (MockedCacheSetCall):

    StripePendingPaymentConsumer().process({'payer_id':'hello_world'})

    assert MockedCacheSetCall.called == True