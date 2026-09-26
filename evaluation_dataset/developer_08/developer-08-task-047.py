def _build_proxy_contract_creation_constructor(self,
                                                   master_copy: str,
                                                   initializer: bytes,
                                                   funder: str,
                                                   payment_token: str,
                                                   payment: int) -> ContractConstructor:
        if not funder or funder == NULL_ADDRESS:
            funder = NULL_ADDRESS
            payment = 0
        return get_paying_proxy_contract(self.w3).constructor(
            master_copy,
            initializer,
            funder,
            payment_token,
            payment)