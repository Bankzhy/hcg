def build(self, owners: List[str], threshold: int, salt_nonce: int,
              gas_price: int, payment_receiver: Optional[str] = None,
              payment_token: Optional[str] = None,
              payment_token_eth_value: float = 1.0, fixed_creation_cost: Optional[int] = None):
        assert 0 < threshold <= len(owners)
        payment_receiver = payment_receiver or NULL_ADDRESS
        payment_token = payment_token or NULL_ADDRESS
        assert Web3.isChecksumAddress(payment_receiver)
        assert Web3.isChecksumAddress(payment_token)
        safe_setup_data: bytes = self._get_initial_setup_safe_data(owners, threshold, payment_token=payment_token,
                                                                   payment_receiver=payment_receiver)
        magic_gas: int = self._calculate_gas(owners, safe_setup_data, payment_token)
        estimated_gas: int = self._estimate_gas(safe_setup_data,
                                                salt_nonce, payment_token, payment_receiver)
        logger.debug('Magic gas %d - Estimated gas %d' % (magic_gas, estimated_gas))
        gas = max(magic_gas, estimated_gas)
        payment = self._calculate_refund_payment(gas,
                                                 gas_price,
                                                 fixed_creation_cost,
                                                 payment_token_eth_value)
        safe_setup_data: bytes = self._get_initial_setup_safe_data(owners, threshold, payment_token=payment_token,
                                                                   payment=payment, payment_receiver=payment_receiver)
        safe_address = self.calculate_create2_address(safe_setup_data, salt_nonce)
        assert int(safe_address, 16), 'Calculated Safe address cannot be the NULL ADDRESS'
        return SafeCreate2Tx(salt_nonce, owners, threshold, self.master_copy_address, self.proxy_factory_address,
                             payment_receiver, payment_token, payment, gas, gas_price, payment_token_eth_value,
                             fixed_creation_cost, safe_address, safe_setup_data)