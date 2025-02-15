from fortuna.conformal.multivalid.batch_mvp import BatchMVPConformalMethod
from fortuna.conformal.regression.base import ConformalRegressor


class BatchMVPConformalRegressor(BatchMVPConformalMethod, ConformalRegressor):
    def __init__(
        self,
    ):
        """
        This class implements a classification version of BatchMVP
        `[Jung et al., 2022] <https://arxiv.org/abs/2209.15145>`_,
        a multivalid conformal prediction method that satisfies coverage guarantees conditioned on group membership
        and non-conformity threshold.
        """
        super().__init__()
